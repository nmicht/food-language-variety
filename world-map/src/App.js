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
      selectedFood: 'almond',
      places: [],
      loading: true,
    };
    this.jsonPath = '../distribution.json';
  };

  componentDidMount = () => {
    this.setState({loading: true});
    this.data.all = this.readJson(this.jsonPath)
      .then((data) => {
        this.data.all = data
        console.log('original data', this.data.all);
        this.data.all.sort(this.compareSynonymFrequency);
        console.log('after sort', this.data.all);
        this.data.images = data.map((o) => {
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


  comparePlaceFrequency(a, b) {
    if (a.places.length > b.places.length) {
      return -1;
    }
    return 1;
  }

  compareSynonymFrequency(a, b) {
    let aSyns = [];
    let bSyns = [];
    aSyns.concat(a.places.map(p => p.synonyms));
    bSyns.concat(b.places.map(p => p.synonyms));

    var aUnique = aSyns.filter( (value, index, self) => {
        return self.indexOf(value) === index;
    } );
    var bUnique = bSyns.filter( (value, index, self) => {
        return self.indexOf(value) === index;
    } );
    console.log(aUnique);
    console.log(bUnique);


   if (aUnique.length > bUnique.length) {
      return 1;
    }
    return -1;
  }

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
