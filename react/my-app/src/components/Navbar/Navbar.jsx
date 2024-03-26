import React from "react";
import { Link } from "react-router-dom";

import "./Navbar.css";


export const Navbar = () => {
    return (
        <nav>
            <Link to='/' ><img className="logo" src='/logo.png' alt="logo" /></Link>
            <div className="nav-main">
                <ul >
                    <li>
                        <div className='dropdown'>
                            <Link to='/' >Транспорт</Link>
                            <div className="dropdown-content">
                                <Link to='/'>Автомобили с пробегом</Link>
                                <Link to='/'>Новые автомобили</Link>
                                <Link to='/'>Электромобили</Link>
                                <Link to='/'>Грузовой транспорт</Link>
                                <Link to='/'>Мототехника</Link>
                                <Link to='/'>Сельхозтехника</Link>
                                <Link to='/'>Спецтехника</Link>
                                <Link to='/'>Прицепы и полуприцепы</Link>
                                <Link to='/'>Автобусы</Link>
                                <Link to='/'>Водный транспорт</Link>
                                <div className="sep-line" />
                                <Link to='/'>Каталог компаний</Link>
                                <Link to='/'>Оценка стоимости автомобиля</Link>
                                <Link to='/'>Каталог модификаций</Link>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div className='dropdown'>
                            <Link to='/parts_and_tyres' >Запчасти и Шины</Link>
                            <div className="dropdown-content">
                                <Link to='/'>Шины и диски</Link>
                                <Link to='/'>Б/у запчасти для авто</Link>
                                <Link to='/'>Весь авто на запчасти</Link>
                                <Link to='/'>Автотовары и расходники</Link>
                            </div>
                        </div>
                    </li>
                    <li>
                        <Link to='/journal'>Журнал</Link>
                    </li>
                    <li>
                        <div className='dropdown'>
                            <Link to='/knowledge'>Знания</Link>
                            <div className="dropdown-content">
                                <Link to='/'>Продажа автомобиля</Link>
                                <Link to='/'>Покупка автомобиля</Link>
                                <Link to='/'>Сделка купли-продажи</Link>
                                <Link to='/'>Налоги и сборы</Link>
                                <Link to='/'>Техосмотр</Link>
                            </div>
                        </div>   
                    </li>
                    <li>
                        <Link to='/finance'>Финансы</Link>
                    </li>
                    <li>
                        <Link to='https://av.by/vin' className="vin">Проверка VIN</Link>
                    </li>
                </ul>
            </div>
            <div className="nav-person">
                <ul >
                    <li>
                        <Link to='/loginPage'>Войти</Link>
                    </li>
                    <li>
                        <Link to='/advertPage' className="advert">Подать объявление</Link>
                    </li>
                </ul>
            </div>

        </nav>

    )
}