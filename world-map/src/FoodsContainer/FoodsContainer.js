import React, { Component } from 'react';
import FoodImage from '../FoodImage/FoodImage'
import './FoodsContainer.css';

class FoodsContainer extends Component {

  renderFoodItem(item, event, selected) {
    return (
      <FoodImage
        key={item.key}
        link={item.image}
        alt={item.key}
        onClick={event}
        selected={selected}
      />
    );
  }

  render(props) {
    const items = this.props.foods.map((i) => {
      return this.renderFoodItem(i, this.props.onClick, this.props.selected);
    });

    return (
      <React.Fragment>
        <p><strong>Selected food:</strong> {this.props.selected}</p>
        <section className="FoodsContainer">
          <ul>
            {items}
          </ul>
        </section>
      </React.Fragment>
    );
  }
}

export default FoodsContainer;
