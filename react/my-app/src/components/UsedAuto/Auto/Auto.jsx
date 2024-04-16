import React, { Suspense, lazy } from 'react';
import { Link } from 'react-router-dom';

import { LazyLoadImage } from "react-lazy-load-image-component";

import './Auto.css'


const Auto = (props) => {

    return (
        <div className="auto">
            <div className='auto-photo'>

                <div className="photos">
                    <LazyLoadImage src={props.auto.main_photo} />
                </div>
            </div>
            <div className='auto-info'>
                <div className='auto-params'>
                    <div className='auto-params-item'>
                        <div className='param-name'>
                            <div className="auto-name">
                                <Link key={props.auto.id} to={`${props.auto.brand}/${props.auto.model}/${props.auto.id}`}>
                                    {props.auto.brand}&nbsp;{props.auto.model}&nbsp;{props.auto.generation_with_years}
                                    </Link>
                            </div>
                        </div>

                        <div className='param-info'>
                            <div className='auto-year'>
                                {props.auto.year} г.
                            </div>

                            <div className='auto-kpp-volume-type_engine'>
                                {props.auto.transmission_type},&nbsp;{props.auto.engine_capacity} л.,&nbsp;{props.auto.engine_type},
                            </div>

                            <div className='auto-kyzov'>
                                {props.auto.body_type}
                            </div>
                            <div className='auto-probeg'>
                                {props.auto.mileage_km} км
                            </div>
                        </div>
                    </div>
                </div>

                <div className='auto-comment'>
                    <span>{props.auto.description.slice(0, 100)}...</span>
                </div>
            </div>

            <div className='auto-price'>
                <div className="auto-price-bel">
                    {props.auto.price_amount_byn} р.
                </div>

                <div className="auto-price-usd">
                    ≈ {props.auto.price_amount_usd} $
                </div>
            </div>

        </div>
    )
}


export default Auto