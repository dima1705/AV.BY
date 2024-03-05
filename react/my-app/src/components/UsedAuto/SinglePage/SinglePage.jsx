import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from 'axios'
import AutoJurnal from "../../AutoJournal/Autojurnal";

import './SinglePage.css'


export const SinglePage = () => {

    const { id } = useParams()
    const [auto, setAuto] = useState([])
    const [photos, setPhotos] = useState([])

    useEffect(() => {
        const getAutoById = async () => {
            const response = await axios.get(`http://localhost:8000/used_cars/{id}?car_id=${id}`)
            setAuto(response.data)
        }

        getAutoById()

        const getPhoto = async () => {
            const response = await axios.get(`http://localhost:8000/used_cars/photos/{id}?car_id=${id}`)
            setPhotos(response.data)
            
        }

        getPhoto()
    
    }, [id])
    // debugger
    console.log(photos)

    return (
        <div className="auto-item">

            <div className="auto-card">
                {auto && (
                    <div className="auto-card-item">
                        <div className="auto-card-name">
                            <div className="auto-card-title">
                                <h1>{auto.name}</h1>
                            </div>
                            <div className="auto-card-date">
                                Опубликовано вчера №{auto.id}{auto.id}{auto.id}
                            </div>
                        </div>
                        <div className="auto-card-info">
                            {/* {photos.map(photo => ( */}
                                <div 
                                key={photos.id} 
                                className="auto-card-photo"
                                style={{backgroundImage: `url(${photos.m_photo})`}}
                                >
                                    {/* {console.log(photo.shift())} */}
                                    {/* <img src={photos.m_photo} /> */}
                                </div>
                            {/* ))} */}

                            <div className="auto-card-params">
                                <div  className="param-price-byn">
                                    {auto.price_for_bel_rub}р.
                                </div>
                                <div className="param-price-usd">
                                    {auto.price_for_usd}$
                                </div>
                                <div className="param-info">
                                    {auto.year},
                                    {auto.kpp},{auto.volume},{auto.type_engine},

                                </div>
                                <div className="param-probeg">
                                    {auto.probeg}
                                </div>
                                <div className="param-dop-info">
                                    {auto.kyzov},
                                    {auto.privod},
                                    {auto.color}
                                </div>
                                <div className="param-power">
                                    {auto.power}
                                </div>

                                <div className="param-buttons">
                                    <button className="dialogs">Написать продавцу</button> 
                                    <button className="phone">Показать телефон</button> 
                                </div>
                            </div>
                        </div>
                        <div className="auto-card-comment">
                            <h4>Описание</h4>
                            <p>{auto.comment}</p>
                                {console.log(auto.power)}
                        </div>
                    </div>
                )
                }
            </div>

            <div className="auto-jurnal">
                <AutoJurnal />
            </div>
        </div>
    )
}