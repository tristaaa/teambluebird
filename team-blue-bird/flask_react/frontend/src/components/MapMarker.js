import React from "react"
import {
    InfoWindow,
    Marker,
} from "google-maps-react";
import {Table, } from "antd"

const locations ={
    C44:{lat: -22.816784, lng:-43.242308},
    C45:{lat: -22.816784, lng:-43.242308},
    C46:{lat: -22.817355, lng:-43.242741},
    C47:{lat: -22.817355, lng:-43.242741},
    C48:{lat: -22.818000, lng:-43.243243},
    C49:{lat: -22.818000, lng:-43.243243},
    C50:{lat: -22.817268, lng:-43.242314},
    C51:{lat: -22.818244, lng:-43.243074},
    C52:{lat: -22.818244, lng:-43.243074},
    C53:{lat: -22.818844, lng:-43.243542},
    C54:{lat: -22.818844, lng:-43.243542},
    C55:{lat: -22.818901, lng:-43.243644},
    C56:{lat: -22.818901, lng:-43.243644},
    C57:{lat: -22.818780, lng:-43.243904},
    C58:{lat: -22.818780, lng:-43.243904},
    C59:{lat: -22.818691, lng:-43.243952},
    C60:{lat: -22.818691, lng:-43.243952},
    C61:{lat: -22.818466, lng:-43.243837},
    C62:{lat: -22.818466, lng:-43.243837},
    C63:{lat: -22.817407, lng:-43.240732},
    C64:{lat: -22.816956, lng:-43.241368},
    C65:{lat: -22.817407, lng:-43.240732},
    C66:{lat: -22.817805, lng:-43.240137},
    C67:{lat: -22.817805, lng:-43.240137},
    C68:{lat: -22.818251, lng:-43.239459},
    C69:{lat: -22.818251, lng:-43.239459},
}

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
            multiple: 2
        }
    },
    {
        title: 'Departure Time',
        dataIndex: 'ScheduledDT',
        sorter:{
            compare: (a,b) => {
                return parseInt(a.ScheduledDT.split(':')[0]) < parseInt(b.ScheduledDT.split(':')[0]) ?  -1 : 1
            },
            multiple: 3
        }
    },
];

export default class MapMarker extends React.Component{
    constructor(props) {
        super(props)
        this.state ={
            isOpen:false,
        }
        console.log('props = ',this.props)
        console.log('Marker recieved data1', this.props.dataSource)
        console.log('Marker recieved data2', this.props.gate)
        this.onToggleOpen = this.onToggleOpen.bind(this)
    }
    onToggleOpen = () => {
        this.setState(({isOpen}) => ({
            isOpen:!isOpen,
        }));
    }
    getPosition(gate){
        let tmpLocation = {}
        Object.keys(locations).forEach(innerKey=> {
            if (innerKey == gate) {
                tmpLocation = locations[innerKey]
                console.log('get gate location', tmpLocation)
                return tmpLocation
            }
        })
    }

    render(){
        return(
            <Marker
                position={this.props.position}
                onClick={this.props.onClick}
            >
                {/*<InfoWindow*/}
                {/*    marker={this.state.activeMarker}*/}
                {/*    visible={this.state.showingInfoWindow}>*/}
                {/*    <div>*/}
                {/*        <p2>{this.props.gate}</p2>*/}
                {/*        <Table columns={columns} dataSource={this.props.dataSource} className="assign-table" />*/}
                {/*    </div>*/}
                {/*</InfoWindow>*/}
            </Marker>

        )
    }
}