import React, { Component } from 'react';
import {Map, TileLayer, Marker, Popup } from 'react-leaflet';
import './WorldMap.css';

class WorldMap extends Component {

  renderMarker(place) {
    const position = [place.lat, place.lng];
    return( 
        <Marker key={position[0]+position[1]} position={position}>
          <Popup>
            {place.name} <br/> {place.synonyms}
          </Popup>
        </Marker>
      )

  }

  render(props) {
    console.log(this.props);
    console.log(this.props.places);
    const markers = this.props.places.map((p) => this.renderMarker(p))
    const zoom = 3;
    const lat = 40.730610;
    const lng = -73.935242;
    const position = [lat, lng];
    return (
      <Map center={position} zoom={zoom}>
        <TileLayer
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
        />
        {markers}
      </Map>
    );
  }
}

export default WorldMap;
