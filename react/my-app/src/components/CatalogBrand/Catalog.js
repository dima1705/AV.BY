import React from 'react';
import { Link } from "react-router-dom";

const Brand = (props) => {
    return (
        <li className='catalog-item'>
            <Link to ='/brand/' className='brand'>
                {props.brand.brand}
            </Link>
        </li>

        
    )
}

export default Brand