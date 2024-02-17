import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
// import UsedAuto from './Used_Auto';

const Auto = (props) => {

    // const {id} = useParams()
    // const [photos, setPhotos] = useState(null)
  
    // useEffect(() => {
    //   const url = (id) => `http://127.0.0.1:8000/used_cars/photos/{id}?car_id=${id}`
  
    //   fetch(url(id))
    //     .then(res => res.json())
    //     .then(res => setPhotos(res))
    // }, [])

    return (
        <tr>
            <td>{props.auto.id}</td>
            {/* <td><img src={photos} alt=""/></td> */}
            <td>{props.auto.name}</td>
            <td>{props.auto.price_for_bel_rub}</td>
            <td>{props.auto.price_for_usd}</td>
            <td>{props.auto.year}</td>
            <td>{props.auto.kpp}</td>
            <td>{props.auto.volume}</td>
        </tr>
    )
}


export default Auto