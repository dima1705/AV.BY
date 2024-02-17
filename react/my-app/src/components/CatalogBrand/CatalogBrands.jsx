import React from "react";

import Brand from "./Catalog";

import './Catalog.css'

export const CatalogBrands = ({ brand }) => {

    return (
        <div className="catalog-brand">
            <ul className="catalog-items">
                {brand.map(brand => <Brand brand={brand} key={brand.id} />)}
            </ul>
            
        </div>
    )
}

export default CatalogBrands