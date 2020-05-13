import React, { useContext, useState, useEffect, useRef } from 'react';
import { Table, AutoComplete, Button, Popconfirm, Form, Select, DatePicker, TimePicker, Upload, message } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import moment from 'moment';
import XLSX from 'xlsx';
import '../styles/FlightForm.css'
import {URL} from "../constants"
import history from './History'
import TopNavBar from "./TopNavBar"
const EditableContext = React.createContext();

class FlightForm extends React.Component {
    constructor(props) {
        super(props);
        this.locations =['Amsterdam','Bogota', 'Buenos Aires', 'Cordoba', 'Lima', 'Miami', 'Montevideo',
            'Rosario', 'Santiago', 'Zurich', 'Campinas', 'Frankfurt', 'Paris',
            'Rome', 'Lisbon', 'Luanda', 'New York', 'Porto',
            'London', 'Panama City', 'Recife', 'Atlanta', 'Dubai',
            'Casablanca', 'Houston', 'Doha', 'Salvador', 'Madrid']
        this.options = []
        for(let i = 0; i < this.locations.length;i++){
            this.options.push({value:this.locations[i]})
        }

        this.columns = [{
            title: 'Flight Number',
            dataIndex: 'number',
            editable: true,
            key:"number",
            render:(text, record) =>{
                return (
                    <input value = {text}
                           placeholder="Add flight number"
                           onChange={(e) => this.handleChange({number:e.target.value}, record)}/>
                );
            },
        },


            {
            title: 'Destination',
            dataIndex: 'dest',
            editable: true,
            key: "dest",
            render:(text, record, idx) =>{

                return (
                    <AutoComplete value = {this.state.dataSource[idx].dest ? this.state.dataSource[idx].dest:null}
                        options={this.options}
                        backfill={true}
                        filterOption={(inputValue, option) =>
                            option.value.toUpperCase().indexOf(inputValue.toUpperCase()) !== -1
                        }
                        onChange={(value) => this.handleChange({dest:value}, record)}
                    >
                        <input 
                               placeholder="Add destination"
                               onChange={(e) => this.handleChange({dest:e.target.value}, record)}
                               />
                    </AutoComplete>

                );
            },
        },{
            title: 'Departure Time',
            dataIndex: 'time',
            editable: true,
            key: "time",
            render:(text, record, idx) =>{
                const format = 'HH:mm';
                return (
                    <TimePicker value={this.state.dataSource[idx].time ? moment(this.state.dataSource[idx].time,format):null}
                                format={format}
                                onChange={(time, timeString) => {console.log("tt",time);this.handleChange({time:timeString}, record)}}
                    />
                );
            },
        },{
            title: 'operation',
            dataIndex: 'operation',
            render: (text, record) =>
                this.state.dataSource.length >= 1 ? (
                    <Popconfirm title="Sure to delete?" onConfirm={() => this.handleDelete(record.key)}>
                        <a>Delete</a>
                    </Popconfirm>
                ) : null,
        },];
        this.state = {
            dataSource: [
                {
                    key: 0,
                    number: "",
                    dest: '',
                    time: '',
                },
            ],
            count: 1,
            date:'',
            currData:{}
        };
        this.handleClickBtn = this.handleClickBtn.bind(this);
    }




    handleClickBtn= (e) =>{
        const formData = new FormData();
        formData.append('date', this.state.date)
        formData.append('data', this.state.dataSource)



        let req_json = {}
        // iterate this.state.dataSource
        req_json = {
            "Date": this.state.date,
            "rows": []
        }

        for(let i=0; i<this.state.dataSource.length; i++){
            let cur = this.state.dataSource[i];
            let tmp = {};
            tmp["Arrival"] = cur["dest"];
            tmp["Schedule_Depart_Time"] = cur["time"];
            tmp["flight_number"] = cur['number'];
            req_json["rows"].push(tmp);

        }
        console.log("json = ", req_json)
        fetch(URL, {
            method: 'POST', // or 'PUT'
            mode: 'cors',
            body: JSON.stringify(req_json), // data can be `string` or {object}!
            headers: new Headers({
                'Content-Type': 'application/json'
            })
        }).then(res => res.json())
            .catch(error => console.error('Error:', error))
            .then(response =>{

                // get the response, and set the data
                console.log(response)
                // response here should already been an obj
                let gateAssign = response['gate_assign']
                let top5 = response['top5']
                let map = response['map']
                this.props.setAssign(gateAssign)
                this.props.setTop(top5)
                this.props.setMap(map)
                history.push("/output")
                // this.props.history.push("/output")
                console.log('Success:', response)
            });
    }

    handleDelete = key => {
        const dataSource = [...this.state.dataSource];
        this.setState({
            dataSource: dataSource.filter(item => item.key !== key),
        });
    };

    handleAdd = () => {
        const { count, dataSource } = this.state;
        const newData = {
            key: count,
            number: "",
            dest: "",
            time: '',
        };
        this.setState({
            dataSource: [...dataSource, newData],
            count: count + 1,
        });
    };
    handleChange = (value, record) =>{
        for(let i in value){
            record[i] = value[i];
            this.setState({
                dataSource: this.state.dataSource.map((item, key) => item.key === record.key ? {...item, [i]: value[i]} : item)
            })
        }
    }

    onDateChange = (date, dateString)=>{
        this.setState({
            date: dateString,
        })
    }

    handleSave = row => {
        const newData = [...this.state.dataSource];
        const index = newData.findIndex(item => row.key === item.key);
        const item = newData[index];
        newData.splice(index, 1, { ...item, ...row });
        this.setState({
            dataSource: newData,
        });
    };

    render() {
      const { dataSource} = this.state;
      const columns = this.columns.map(col => {
          if (!col.editable) {
              return col;
          }

          return {
              ...col,
              onCell: record => ({
                  record,
                  editable: col.editable,
                  dataIndex: col.dataIndex,
                  title: col.title,
                  handleSave: this.handleSave,
              }),
          };
      });

    function sheet_to_json(sheet, header) {
      if(sheet == null || sheet["!ref"] == null) return [];
      var val = {t:'n',v:0}, offset = 1;
      var r = {s:{r:0,c:0},e:{r:0,c:0}};
      var range = sheet["!ref"];
      switch(typeof range) {
        case 'string': r = XLSX.utils.decode_range(range); break;
        case 'number': r = XLSX.utils.decode_range(sheet["!ref"]); r.s.r = range; break;
        default: r = range;
      }
      var cols = [];
      var out = [];
      var R = r.s.r, C = 0;
      for (R = r.s.r + offset; R <= r.e.r+offset; ++R){
        var row = {}
        for(C = r.s.c; C <= r.e.c; ++C) {
          cols[C] = XLSX.utils.encode_col(C);
          val = sheet[cols[C] + R];
          row[header[C]]=val.w 
        }
        out[R-1]=row
      }
      return out;
    }

    const props = {
      name: 'file',
      headers: {
        authorization: 'authorization-text',
      },
      accept: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      showUploadList: false,
      className:"upload",
      beforeUpload: (file) => {
        const { count, dataSource } = this.state;
        var reader = new FileReader();
        var result;
        var thiso = this;
        reader.onload = function (e) {
            var data = e.target.result;
            var workbook = XLSX.read(data, {type: 'array'});
            var first_worksheet = workbook.Sheets[workbook.SheetNames[0]];
            var header = ["number","dest","time"];
            result = sheet_to_json(first_worksheet, header);
            result.forEach((x,i)=>x["key"]=i);
            thiso.setState({
              dataSource: result,
              count: result.length
            });
        };
        reader.readAsArrayBuffer(file);
        return false;
      }
    };
    return (
        <div>
            <TopNavBar></TopNavBar>
            <div className='main'>

                <h1>Please select a date and fill all flight information to get an assignment</h1>
                <h3>Can also upload an Excel sheet without header to fill the form</h3>
                <Button
                    onClick={this.handleAdd}
                    type="primary"
                    className='add-btn'
                >
                    Add a row
                </Button>
                <DatePicker
                    className={"date-picker"}
                    onChange={this.onDateChange}/>

                <Upload {...props}>
                  <Button>
                    <UploadOutlined /> Upload an Excel Sheet
                  </Button>
                </Upload>

                <Table
                    rowClassName={() => 'editable-row'}
                    bordered
                    dataSource={dataSource}
                    columns={columns}
                />
                <Button
                    onClick={this.handleClickBtn}
                > Submit</Button>
            </div>
        </div>
    );
  }
}


export default FlightForm;
