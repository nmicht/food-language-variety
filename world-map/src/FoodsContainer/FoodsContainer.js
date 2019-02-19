import React, { Component } from 'react';
import FoodImage from '../FoodImage/FoodImage'
import './FoodsContainer.css';

class FoodsContainer extends Component {

  renderFoodItem(item, event) {
    return (
      <FoodImage
        key={item.key}
        link={item.image}
        alt={item.key}
        onClick={event}
      />
    );
  }

  render(props) {
    const items = this.props.foods.map((i) => {
      return this.renderFoodItem(i, this.props.onClick);
    });

    return (
      <section className="Foods">
      <h2>Food names</h2>
      <ul>
        {items}
      </ul>
      </section>
    );
  }
}

export default FoodsContainer;
