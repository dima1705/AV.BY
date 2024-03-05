import React from "react";

import './AutoJurnal.css'

export const AutoJurnal = () => {

    return (
        <div className="add-container">
                <div className="news">
                    <h1 className="news-title">
                        Автожурнал
                    </h1>
                    <div className="news-items">
                        <div className="news-item">
                        Белорусы открыли СТО в Испании, однако власти бизнес закрыли. Почему?
                            <div className="news-meta">
                                <span className="news-category">Авторынок</span>
                                <span className="news-date">3 часа назад</span>
                            </div>
                        </div>
                        <div className="news-item">
                            Mazda показала новый кроссовер CX-70
                            <div className="news-meta">
                                <span className="news-category">Авторынок</span>
                                <span className="news-date">3 часа назад</span>
                            </div>
                        </div>
                        <div className="news-item">
                        Новинки от BELGEE, и что будет с утильсбором в Беларуси. Подводим итоги большой пресс-конференции БАА
                            <div className="news-meta">
                                <span className="news-category">Авторынок</span>
                                <span className="news-date">3 часа назад</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    )
}

export default AutoJurnal