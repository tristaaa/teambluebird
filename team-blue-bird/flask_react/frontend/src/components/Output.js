import {Button, Table, Typography} from 'antd';
import React from 'react';
import '../styles/Output.css';
import {MinusCircleTwoTone, PlusCircleTwoTone} from '@ant-design/icons'
import BackwardOutlined from "@ant-design/icons/lib/icons/BackwardOutlined"
import history from './History'
import TopNavBar from "./TopNavBar"
const { Text } = Typography;

const columns = [
    {
        title: 'Flight Number',
        dataIndex: 'number',
        sorter:{
            compare: (a,b) => {
                return a.number < b.number ?  -1 : 1
            },
            multiple: 1
        }
    },
    {
        title: 'Destination',
        dataIndex: 'dest',
        sorter:{
            compare: (a,b) => {
                return a.dest < b.dest ?  -1 : 1
            },
            multiple: 3
        }
    },
    {
        title: 'Scheduled Departure Time',
        dataIndex: 'ScheduledDT',
        sorter:{
            compare: (a,b) => {
                return parseInt(a.ScheduledDT.split(':')[0]) < parseInt(b.ScheduledDT.split(':')[0]) ?  -1 : 1
            },
            multiple: 4
        }
    },
    {
        title: 'Gate',
        dataIndex: 'gate',
        sorter:{
            compare: (a,b) => {
                return parseInt(a.gate.slice(1)) < parseInt(b.gate.slice(1)) ?  -1 : 1
            },
            multiple: 2
        }
    },
];

const gateColumns = [
    {
        title: 'Flight Number',
        dataIndex: 'number',
        sorter:{
            compare: (a,b) => {
                return a.number < b.number ?  -1 : 1
            },
        }
    },
    {
        title: 'Destination',
        dataIndex: 'dest',
        sorter:{
            compare: (a,b) => {
                return a.dest < b.dest ?  -1 : 1
            },
        }
    },
    {
        title: 'Scheduled Departure Time',
        dataIndex: 'ScheduledDT',
        sorter:{
            compare: (a,b) => {
                return parseInt(a.ScheduledDT.split(':')[0]) < parseInt(b.ScheduledDT.split(':')[0]) ?  -1 : 1
            },
        }
    },
];

class Output extends React.Component{
    constructor(props) {
        super(props);
        this.onChange = this.onChange.bind(this);
        this.handleClickBtn = this.handleClickBtn.bind(this);
        this.state={
            upperData:[],
            downData1:[],
            downData2:[],
            shownDownData:[],
        }
        let assignTable = this.props.assign_table
        let top5Table = this.props.top5_table
        // fill data into assign table
        Object.keys(assignTable).forEach(key => {
            let tempItem = {}
            let tempArr = assignTable[key]
            tempItem.key = key  // take off
            Object.keys(tempArr).forEach(key =>{
                if(key == 'flight_No'){
                    tempItem.number = tempArr[key]
                } else if(key == 'dest'){
                    tempItem.dest = tempArr[key]
                } else if(key == 'ScheduledDT'){
                    tempItem.ScheduledDT = tempArr[key]
                } else if(key == 'gate'){
                    tempItem.gate = tempArr[key]
                }
            })
            this.state.upperData.push(tempItem)
        })
        // fill data into top5 table
        let count = 0
        Object.keys(top5Table).forEach(key =>{
            let tempItem = {}
            let layer1 = top5Table[key]
            tempItem.key = key
            tempItem.number = key
            tempItem.dest = layer1[0]['dest']
            tempItem.ScheduledDT = layer1[0]['ScheduledDT']
            this.state.downData1.push(tempItem)
            for(let i = 0; i < layer1.length; i++){
                let innerTmp = {}
                innerTmp.key = count
                innerTmp.number = key
                Object.keys(layer1[i]).forEach(innerKey =>{
                    if(innerKey == 'gate'){
                        innerTmp.gate = layer1[i][innerKey]
                    } else if(innerKey == 'shopTime'){
                        innerTmp.shopTime = layer1[i][innerKey]
                    }
                })
                this.state.downData2.push(innerTmp)
                count++
            }
        })
        console.log('output construction complete!')
        // this.onExpand = this.onExpand.bind(this)
        this.expandedRowRender = this.expandedRowRender.bind(this)
    }

    handleClickBtn(){
        history.push("/map")
    }
    handleBack(){
        history.push("/")
    }
    onChange(pagination, filters, sorter, extra) {
    }

    expandedRowRender(record){
        const columns = [
            {
                title: 'Gate',
                dataIndex: 'gate',
                sorter:{
                    compare: (a,b) => {
                        return parseInt(a.gate.slice(1)) < parseInt(b.gate.slice(1)) ?  -1 : 1
                    },
                }
            },
            {
                title: 'Increased Shopping Time (Minutes)',
                dataIndex: 'shopTime',
                sorter: {
                    compare: (a, b) => a.shopTime - b.shopTime,
                    multiple: 1
                }
            },
        ];
        const data = []
        let dataSource = this.state.downData2
        for(let i = 0; i < dataSource.length; i++){
            if(dataSource[i].number == record.number){
                data.push(dataSource[i])
            }
        }
        return <Table columns={columns} dataSource={data} pagination={false} />;
    }

    render(){

        return(
            <div>
                <TopNavBar></TopNavBar>
                <div className='main'>
                    <h1> Assignment Recommendation</h1>
                    <div>
                        <Button
                            onClick={this.handleBack}
                            type={"primary"}
                            className='back_button'
                        >
                            Go Back
                        </Button>
                        <Button onClick={this.handleClickBtn}
                                type={"primary"}
                                className='map_button'
                        > View in Map</Button>
                    </div>
                    <Table columns={columns} dataSource={this.state.upperData} onChange={this.onChange} className="assign-table" />
                    <h1> Recommended Gates</h1>
                    <Table className="components-table-demo-nested"
                           columns={gateColumns}
                        // rowKey={record => record.number}
                           expandable={{
                               // onExpand: (record) =>
                               expandedRowRender: (record) => this.expandedRowRender(record),
                               expandIcon: ({ expanded, onExpand, record }) =>
                                   expanded ? (
                                       <MinusCircleTwoTone onClick={e => onExpand(record, e)} />
                                   ) : (
                                       <PlusCircleTwoTone onClick={e => onExpand(record, e)} />
                                   )
                           }}
                           dataSource={this.state.downData1}
                           onChange={this.onChange} />
                </div>
            </div>
        );
    }
}
export default Output;