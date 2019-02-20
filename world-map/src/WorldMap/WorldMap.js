import React, { Component } from 'react';
import {Map, TileLayer, Marker, Popup } from 'react-leaflet';
import './WorldMap.css';

class WorldMap extends Component {
  render(props) {
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
        <Marker position={position}>
          <Popup>
            A pretty CSS3 popup. <br/> Easily customizable.
          </Popup>
        </Marker>
      </Map>
    );
  }
}

export default WorldMap;
