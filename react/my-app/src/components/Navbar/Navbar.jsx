import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../../providers/AuthProvider";
// import {LoginPage} from '../../pages/Auth/Login/LoginPage'

import "./Navbar.css";


export const Navbar = () => {

    const {user, logout} = useContext(AuthContext)

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
                    {!user && (
                        <li>
                            <Link to='/loginPage'>Войти</Link>
                        </li>
                    )}
                    {user && (
                        <li>
                            <div className='dropdown'>
                                <Link to='/profile' className="nav-profile-link">
                                    <span className="profile-icon">
                                        <svg aria-hidden="true" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg" fill="currentcolor">
                                            <path d="M12 18a6 6 0 1 0 0-12 6 6 0 0 0 0 12zm0 2a8 8 0 1 1 0-16 8 8 0 0 1 0 16zm-5-3.878a53.447 53.447 0 0 1 3.059-.839c.543-.143.543-.505.543-.8 0-.343-.156-.658-.302-.896a2.38 2.38 0 0 1-.293-.848.258.258 0 0 0-.104-.172c-.094-.066-.272-.295-.387-.762-.094-.372-.052-.448-.01-.524.021-.029.031-.067.042-.105.073-.219-.011-.953-.105-1.363-.041-.181.105-2.422 3.001-1.653 1.813 0 1.855 1.472 1.813 1.644-.094.41-.177 1.134-.104 1.363.01.038.031.066.041.104.042.077.073.162-.01.525-.115.466-.292.695-.386.762-.063.048-.105.105-.105.171a2.447 2.447 0 0 1-.292.849c-.178.305-.303.667-.303.905 0 .295 0 .657.543.8.929.22 2.339.629 3.049.858 0 0-1.003 2.12-4.845 2.12C8.003 18.261 7 16.122 7 16.122z"></path>
                                        </svg>
                                    </span>
                                </Link>
                                <div className="dropdown-content">
                                    <div className="profile-dropdown-name">
                                        <h4 className="profile-dropdown-title">
                                            {user.username.slice(7)}
                                        </h4>
                                    </div>
                                    <Link to='/'>Мои объявления</Link>
                                    <Link to='/'>История заказов</Link>
                                    <Link to='/'>Настройки</Link>
                                    <Link to='/'>Предупреждения</Link>
                                    <Link to='/'>
                                        <div>
                                            <svg aria-hidden="true" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg" fill="currentcolor">
                                                <path d="M6 6.5v11a.5.5 0 0 0 .5.5h6a.5.5 0 0 0 .5-.5v-11a.5.5 0 0 0-.5-.5h-6a.5.5 0 0 0-.5.5zM15 9h-2v6h2v4a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v4zm1.925 2l-.005-1.471a.5.5 0 0 1 .807-.396l3.225 2.514a.499.499 0 0 1 0 .789l-3.207 2.497a.5.5 0 0 1-.807-.393L16.933 13H9a1 1 0 0 1 0-2h7.925z"></path>
                                            </svg>
                                            <span onClick={logout}>Выйти</span>
                                        </div>
                                    </Link>
                                </div>
                            </div>

                            {/* <div className="profile-dropdown">
                                <div className="profile-dropdown-name">
                                    <h4 className="profile-dropdown-title">
                                        {auth.userName}
                                    </h4>
                                </div>
                            </div>
                            <div className="profile-dropdown-content">
                                <ul className="profile-dropdown-list">
                                    <li className="profile-dropdown-item">
                                        <Link to='' className="profile-dropdown-link">
                                            <span className="profile-dropdown-text">Мои объявления</span>
                                        </Link>
                                    </li>
                                    <li className="profile-dropdown-item">
                                        <Link to='' className="profile-dropdown-link">
                                            <span className="profile-dropdown-text">История заказов</span>
                                        </Link>
                                    </li>
                                    <li className="profile-dropdown-item">
                                        <Link to='' className="profile-dropdown-link">
                                            <span className="profile-dropdown-text">Настройки</span>
                                        </Link>
                                    </li>
                                    <li className="profile-dropdown-item">
                                        <Link to='' className="profile-dropdown-link">
                                            <span className="profile-dropdown-text">Предупреждения</span>
                                        </Link>
                                    </li>
                                    <li className="profile-dropdown-item">
                                        <Link to='' className="profile-dropdown-link">
                                            <div>
                                                <svg aria-hidden="true" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg" fill="currentcolor">
                                                    <path d="M6 6.5v11a.5.5 0 0 0 .5.5h6a.5.5 0 0 0 .5-.5v-11a.5.5 0 0 0-.5-.5h-6a.5.5 0 0 0-.5.5zM15 9h-2v6h2v4a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v4zm1.925 2l-.005-1.471a.5.5 0 0 1 .807-.396l3.225 2.514a.499.499 0 0 1 0 .789l-3.207 2.497a.5.5 0 0 1-.807-.393L16.933 13H9a1 1 0 0 1 0-2h7.925z"></path>
                                                </svg>
                                                <span >Выйти</span>
                                            </div>
                                            
                                        </Link>
                                    </li>
                                </ul>
                            </div> */}
                        </li>
                    )}
                    {user && (
                        <li>
                            <Link to='/advertPage' className="advert">Подать объявление</Link>
                        </li>
                    )}
                    {!user && (
                        <li>
                            <Link to='/loginPage' className="advert">Подать объявление</Link>
                        </li>
                    )}

                </ul>
            </div>

        </nav>

    )
}