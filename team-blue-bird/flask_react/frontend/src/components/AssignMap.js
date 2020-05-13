
// lat -22.817485 lng:-43.242700 zoom:18 key:AIzaSyAXvHpbhJ9M4-ZJQPEDMRdJTFPW4BYsriQ
import React from 'react';
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';
import {Table, Button} from "antd"
import '../styles/AssignMap.css'
import MapMarker from "./MapMarker"
import styles from '../styles/AssignMap.css'
import BackwardOutlined from "@ant-design/icons/lib/icons/BackwardOutlined"
import TopNavBar from "./TopNavBar"
import history from './History'



const locations ={
    C44:{lat: -22.816784, lng:-43.242308},
    C45:{lat: -22.816806, lng:-43.242328},
    C46:{lat: -22.817329, lng:-43.242729},
    C47:{lat: -22.817377, lng:-43.242766},
    C48:{lat: -22.817975, lng:-43.243227},
    C49:{lat: -22.818018, lng:-43.243263},
    C50:{lat: -22.817268, lng:-43.242314},
    C51:{lat: -22.818222, lng:-43.243063},
    C52:{lat: -22.818269, lng:-43.243095},
    C53:{lat: -22.818815, lng:-43.243523},
    C54:{lat: -22.818861, lng:-43.243556},
    C55:{lat: -22.818891, lng:-43.243607},
    C56:{lat: -22.818904, lng:-43.243682},
    C57:{lat: -22.818806, lng:-43.243871},
    C58:{lat: -22.818771, lng:-43.243923},
    C59:{lat: -22.818724, lng:-43.243961},
    C60:{lat: -22.818655, lng:-43.243978},
    C61:{lat: -22.818433, lng:-43.243825},
    C62:{lat: -22.818466, lng:-43.243837},
    C63:{lat: -22.816956, lng:-43.241368},
    C64:{lat: -22.817704, lng:-43.240732},
    C65:{lat: -22.817407, lng:-43.240732},
    C66:{lat: -22.817805, lng:-43.240137},
    C67:{lat: -22.817853, lng:-43.240067},
    C68:{lat: -22.818251, lng:-43.239459},
    C69:{lat: -22.818280, lng:-43.239407},
}

const columns = [
    {
        title: 'Flight Number',
        dataIndex: 'number',
        sorter:{
            compare: (a,b) => a.number - b.number,
            multiple: 3
        }
    },
    {
        title: 'Destination',
        dataIndex: 'dest',
        sorter:{
            compare: (a,b) => a.dest - b.dest,
            multiple: 3
        }
    },
    {
        title: 'Departure Time',
        dataIndex: 'ScheduledDT',
        sorter:{
            compare: (a,b) => a.ScheduledDT - b.ScheduledDT,
            multiple: 2
        }
    },
];


export class AssignMap extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            showingInfoWindow: false,
            activeMarker: {},
            selectedGate: {},
            info_data: []
        }
        Object.keys(this.props.map_table).forEach(key =>{
            console.log('map row data = ', props.map_table[key])
            Object.keys(locations).forEach(innerKey=>{
                if(innerKey == key){
                    console.log('inner key = ', innerKey)
                }
            })
        })
        console.log('Object keys = ',Object.keys(this.props.map_table))
    }

    onMarkerClick = (props, marker, e) =>{
        this.setState({
            selectedGate: marker.text,
            activeMarker: marker,
            showingInfoWindow: true,
            info_data:this.props.map_table[marker.text]
        });
        console.log('dataSource =', this.state.info_data)
    }


    onMapClicked = (props) => {
        if (this.state.showingInfoWindow) {
            this.setState({
                showingInfoWindow: false,
                activeMarker: null
            })
        }
    };

    handleClick(){
        history.push("/output")
    }

    render() {
        return (
            <div>
                <TopNavBar/>
                <Button
                    className='button'
                    type='primary'
                    onClick={this.handleClick}
                >Go Back</Button>
                <div className='main'>
                    <Map
                        containerStyle={{
                            height: '100vh',
                            position: 'relative',
                            width: '100%'
                        }}
                        google={this.props.google}
                        initialCenter={{
                            lat: -22.817485,
                            lng: -43.242700
                        }}
                        zoom={18}
                        onClick={this.onMapClicked}>
                        {Object.keys(this.props.map_table).map(gate =>(
                                <Marker
                                    key={gate}
                                    position={locations[gate]}
                                    onClick={this.onMarkerClick}
                                    text={gate}
                                >
                                </Marker>
                            )
                        )}

                        <InfoWindow
                            marker={this.state.activeMarker}
                            visible={this.state.showingInfoWindow}>
                            <div>
                                <p2>{this.state.selectedGate}</p2>
                                <Table columns={columns} dataSource={this.state.info_data} onChange={this.onChange} className="assign-table" />
                            </div>
                        </InfoWindow>
                    </Map>
                </div>
            </div>
        )
    }
}

export default GoogleApiWrapper({
    // googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyD3CEh9DXuyjozqptVB5LA-dN7MxWWkr9s&v=3.exp&libraries=geometry,drawing,places"
    // apiKey: ("AIzaSyAXvHpbhJ9M4-ZJQPEDMRdJTFPW4BYsriQ")
})(AssignMap)