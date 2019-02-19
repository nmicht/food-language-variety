import React from 'react';
import './FoodImage.css';

export default function FoodImage(props) {
  return (
    <li>
      <img
        src={props.link}
        alt={props.alt}
        onClick={(e) => props.onClick(e)}
      />
    </li>
  );
}
