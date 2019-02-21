import React from 'react';
import './FoodImage.css';

export default function FoodImage(props) {
  const isSelected = props.selected === props.alt;
  return (
    <li className={isSelected ? 'selected' : ''}>
      <img
        src={props.link}
        alt={props.alt}
        onClick={(e) => props.onClick(e)}
      />
    </li>
  );
}
