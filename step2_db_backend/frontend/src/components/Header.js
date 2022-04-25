import {HashRouter, Route, NavLink, Switch, Redirect} from 'react-router-dom'


export default function Header({is_authenticated, logout, token}) {
    let loginButton = ''
    if(token === ''){
        loginButton = <NavLink className="nav-link" to='/login'> login </NavLink>
    }else{
        loginButton = <button className="buttt nav-link " onClick={() => logout()}> logout </button>
    }

    return(
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
              <div className="container-fluid">
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                              <NavLink className="nav-link" to='/'> список пользователей</NavLink>
                            </li>
                            <li className="nav-item">
                              <NavLink className="nav-link" to='/projects'> проекты</NavLink>
                            </li>

                            <li className="nav-item">
                              <NavLink className="nav-link" to='/todos'> todo заметки</NavLink>
                            </li>
                            <li>
                                {loginButton}
                            </li>
                      </ul>
                </div>
              </div>
            </nav>

    )
}
