import React, { Component } from 'react';
import L from 'leaflet'
import {Map, TileLayer, Marker, Popup } from 'react-leaflet';
import './WorldMap.css';

class WorldMap extends Component {
  constructor(props) {
    super(props);
    this.colors = [
      'green',
      'red',
      'blue',
      'orange'
    ]
    this.markers = {
      green: L.icon({
          iconUrl: 'iconGreen.png',
          iconSize: [20, 20],
      }),
      red: L.icon({
          iconUrl: 'iconRed.png',
          iconSize: [20, 20],
      }),
      blue: L.icon({
          iconUrl: 'iconBlue.png',
          iconSize: [20, 20],
      }),
      orange: L.icon({
          iconUrl: 'iconOrange.png',
          iconSize: [20, 20],
      }),
    }
  }


  renderMarker(place, color) {
    const position = [place.lat, place.lng];
    return(
        <Marker key={position[0]+position[1]} position={position} icon={this.markers[color]}>
          <Popup>
            {place.name} <br/> {place.synonyms}
          </Popup>
        </Marker>
      )

  }

  render(props) {
    // console.log(this.props);
    // console.log(this.props.places);
    const markerColors = {}
    let currentColorIndex = 0
    const markers = this.props.places.map((p) => {
      console.log(p.synonyms);
      let color;
      for (let s of p.synonyms) {
        if(markerColors.hasOwnProperty(s)){
          color = markerColors[s];
        } else {
          markerColors[s] = this.colors[currentColorIndex]
          color = markerColors[s];
          currentColorIndex += 1;
        }
        console.log(markerColors);
      }
      return this.renderMarker(p, color)
    })
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
