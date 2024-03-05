import React, { Suspense, lazy} from 'react';
import { Link } from 'react-router-dom';

import { LazyLoadImage } from "react-lazy-load-image-component";
import axios from 'axios'

import './Auto.css'

const Photo = lazy(() => import('./Photo'))


const Auto = (props) => {

    return (
        <div className="auto">
            <div className='auto-photo'>

                <Suspense fallback={<div>Loading...</div>}><Photo auto={props.auto} /></Suspense>

            </div>
            <div className='auto-info'>
                <div className='auto-params'>
                    <div className='auto-params-item'>
                        <div className='param-name'>
                            <div className="auto-name">
                                <Link key={props.auto.id} to={`${props.auto.name}/${props.auto.id}`}>{props.auto.name}</Link>
                            </div>
                        </div>

                        <div className='param-info'>
                            <div className='auto-year'>
                                {props.auto.year}
                            </div>

                            <div className='auto-kpp-volume-type_engine'>
                                {props.auto.kpp}{props.auto.volume}{props.auto.type_engine}
                            </div>

                            <div className='auto-kyzov'>
                                {props.auto.kyzov}
                            </div>
                            <div className='auto-probeg'>
                                {props.auto.probeg}
                            </div>
                        </div>
                    </div>
                </div>

                <div className='auto-comment'>
                    <span>{props.auto.comment.slice(0, 100)}...</span>
                </div>
            </div>

            <div className='auto-price'>
                <div className="auto-price-bel">
                    {props.auto.price_for_bel_rub}р.
                </div>

                <div className="auto-price-usd">
                    {props.auto.price_for_usd}$
                </div>
            </div>

        </div>
    )
}


export default Auto