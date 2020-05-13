import React from 'react';
import {
    withScriptjs,
    withGoogleMap,
    GoogleMap,
} from "react-google-maps";
import MapMarker from "./MapMarker"

class NewMap extends React.Component {
    constructor(props) {
        super(props);
        this.state ={
            dataSource:[]
        }
        console.log('recieved data =', this.props.map_table)
    }

    reloadMarkers = () => {
        const center = this.map.getCenter();
        const position = { latitude: center.lat(), longitude: center.lng() };

        const bounds = this.map.getBounds();
        const northEast = bounds.getNorthEast();
        const east = new window.google.maps.LatLng(center.lat(), northEast.lng());
        const range =
            window.google.maps.geometry.spherical.computeDistanceBetween(center, east)
            / 1000;

        this.props.onChange(position, range);
    }

    saveMapRef = (mapInstance) => {
        this.map = mapInstance;
        window.map = mapInstance;
    }
    render() {
        // console.log({ lat: position.latitude, lon: position.longitude })
        return (
            <GoogleMap
                ref={this.saveMapRef}
                googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyD3CEh9DXuyjozqptVB5LA-dN7MxWWkr9s&v=3.exp&libraries=geometry,drawing,places"
                loadingElement={<div style={{ height: `100%` }} />}
                defaultZoom={18}
                defaultCenter={{ lat: -22.817485, lng: -43.242700}}
                onDragEnd={this.reloadMarkers}
                onZoomChanged={this.reloadMarkers}
            >
                {/*{this.props.posts.map((post) => (*/}
                {/*    <MapMarker*/}
                {/*        post={post}*/}
                {/*        key={post.url}*/}
                {/*    />*/}
                {/*))}*/}
            </GoogleMap>
        );
    }
}
export const MarkerMap = withScriptjs(withGoogleMap(NewMap));