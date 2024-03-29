import React from "react";


import './Catalog.css'
import { Link } from "react-router-dom";

export const CatalogBrands = (props) => {
    // debugger
    return (
        // <div className="catalog-brand">
            // <ul className="catalog-items">
                <li className='catalog-item'>
                    <Link to='/brand/' className='brand'>
                        <span className='catalog-title'>{props.brand.brand}</span>
                    </Link>
                </li>
            // </ul>

        // </div>
    )
}

export default CatalogBrands