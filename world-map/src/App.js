import React, { Component } from 'react';
import FoodsContainer from './FoodsContainer/FoodsContainer';
import WorldMap from './WorldMap/WorldMap';
// import Map from './Map/Map'

import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.data = {
      images: [],
      all: {}
    };
    this.state = {
      selectedFood: 'ALMOND',
      places: [],
      loading: true,
    };
    this.jsonPath = '../distribution.json';
  };

  componentDidMount = () => {
    this.setState({loading: true});
    this.data.all = this.readJson(this.jsonPath)
      .then((data) => {
        this.data.all = data.filter((e) => e.places.length > 0)
        this.data.images = this.data.all.map((o) => {
          const n = {
            key: o.key,
            image: o.image
          }
          return n;
        });
        console.log('The data was loaded', this.data.all, this.data.images);
        this.setState({loading: false});
      });
  };

  handleClick = (el) =>  {
    this.setState({
      selectedFood: el.currentTarget.alt,
      places: (this.data.all.find((o) => o.key===el.currentTarget.alt)).places
    });
  }

  readJson(path) {
     return fetch(path)
     .then(response => {
         if (!response.ok) {
             throw new Error("HTTP error " + response.status);
         }
         return response.json();
     })
     .catch(function () {
         this.dataError = true;
     })
  }

  render() {
    if (this.state.loading === true) {
      return <h2>Loading...</h2>;
    }
  

    return (
      <React.Fragment>
        <header>
          <h1>Food distribution</h1>
        </header>
        <main>
          <aside>
            <FoodsContainer
              foods={this.data.images}
              onClick={this.handleClick}
              selected={this.state.selectedFood}
            />
          </aside>
          <WorldMap places={this.state.places} />
        </main>
      </React.Fragment>
    );
  }
}

export default App;
