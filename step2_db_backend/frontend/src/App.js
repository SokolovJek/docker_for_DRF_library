import './App.css';
import React from 'react';
import axios from 'axios'
import {HashRouter,BrowserRouter, Route, NavLink, Switch, Redirect} from 'react-router-dom'
import Cookies from 'universal-cookie'

import ProjectsList from './components/Project.js'
import TodosList from './components/Todo.js'
import ProjectsTodo from './components/ProjectTodo.js'
import LoginForm from './components/Auth.js'
import AuthorList from './components/Author.js'
import Header from './components/Header.js'
import Footer from './components/Footer.js'
import ToDoForm from './components/ToDoForm.js'
import ProjectForm from './components/ProjectForm.js'


const page_not_found_404 = function(location){
    return(
        <div>
            <h1>К сожалению данная страница '{location.pathname}' отсутствует, проверте корректность указаного адреса.</h1>
        </div>
    )
}


class App extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			'users': [],
			'projects': [],
			'todos': [],
			'token': '',
			'text': '',
			'findProject': [],
		};
		this.is_authenticated = this.is_authenticated.bind(this);
		this.logout = this.logout.bind(this);
	}


    deleteToDo(id){
        console.log('todo delete', id)
        const headers = this.get_headers()
        axios.delete(`http://151.248.126.250:8000/api/todo/${id}/`, {headers} )
        .then(response => {this.setState({'todos': this.state.todos.filter((todo) => todo.id !== id )} )})
        .catch(error => console.log(error))
    }


    createToDo(description, project, user){
        user = this.state.users.filter((item) => item.id == user)[0]
        project = this.state.projects.filter((item) => item.id == project )[0]

        const headers = this.get_headers()
        const data = {"todo_descriptions": description,
        "users": user.id,
        "project": project.id
        }
        axios.post('http://151.248.126.250:8000/api/todo/', data, {headers:headers})
        .then(response => {
            let todo = response.data
            this.setState(prevState => (
                {todos: [...prevState.todos, todo]}
                ))
            })
        .catch(error => console.log(error))
    }


    deleteProject(id){
        const headers = this.get_headers()
        axios.delete(`http://151.248.126.250:8000/api/projects/${id}/`, {headers} )
        .then(response => {this.setState({'projects': this.state.projects.filter((project) => project.id !== id )} )})
        .catch(error => console.log(error))
    }


    createProject(project_name, users, link_git, descriptions){
        users = this.state.users.filter((item) => item.id === Number(users))[0]
        const headers = this.get_headers()
        const data = {
            "project_name": project_name,
            "users": [users.id],
            "link_git": link_git,
            "descriptions": descriptions
        }
        axios.post('http://151.248.126.250:8000/api/projects/', data, {headers:headers})
        .then(response => {
            let project = response.data
            this.setState(prevState => (
                {projects: [...prevState.projects, project]}
                ))
            })
        .catch(error => console.log(error))
    }


    findText(text){
        this.setState({'text': text});
        this.findProjectFrontend(text)
    }


    findProjectFrontend(text){
        let findProject = this.state.findProject
        if(text !== ''){
            findProject = findProject.filter( (project) =>
                project.project_name.toLowerCase().includes(text.toLowerCase()))
            }
        this.setState({'projects': findProject})
    }


	set_token(token){
	    const cookies = new Cookies()
	    cookies.set('token', token)
	    this.setState({'token': token}, () => this.load_data())
	}


    get_token_from_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }


    is_authenticated(){
        return this.state.token != ''
    }


    logout(){
        this.set_token('');
    }


	get_token(username, password){
        axios.post('http://151.248.126.250:8000/api-token-auth/', {username:username, password:password})
        .then(response => {
            this.set_token(response.data['token'])
            })
        .catch(error => alert('Неверный логин или пароль'))
    }


    get_headers(){
        let headers = {'Content-Type': 'application/json'}
        if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


    load_data(){
        const headers = this.get_headers()
        axios.get('http://151.248.126.250:8000/api/users/', {headers})
			.then(response => {
				const users = response.data
				this.setState(
					{ 'users': users }
				)
			}).catch(error => {console.log('--my--error-' + error)
			                   this.setState({users: []})
			 })


		axios.get('http://151.248.126.250:8000/api/projects/', {headers})
			.then(response => {
				const projects = response.data
				this.setState(
					{ 'projects': projects }
				)
				this.setState(
					{ 'findProject': projects }
				)

			}).catch(error => {console.log('--my--error-' + error)
			                   this.setState({projects: []})
			 })


	    axios.get('http://151.248.126.250:8000/api/todo/', {headers})
			.then(response => {
				const todos = response.data
				this.setState(
					{ 'todos': todos }
				)
			}).catch(error => {console.log('--my-todo-error-' + error)
			                   this.setState({todos: []})
			 })

    }


	componentDidMount() {
		this.get_token_from_storage()
	}


	render() {
		return (
			<div className='container'>
                <BrowserRouter>

                   <Header/>
                   <nav>
                        <ul>
                            <li>
                                <NavLink to='/'> список пользователей</NavLink>
                            </li>
                            <li>
                                <NavLink to='/projects'> проэкты </NavLink>
                            </li>
                            <li>
                                <NavLink to='/todos'> todo </NavLink>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}> logout </button> :
                                    <NavLink to='/login'> login </NavLink>}
                            </li>
                        </ul>
                    </nav>

                    <div className='row'>
                        <div className='col-12'>
                            <h1 className='text-center text-white'>
                                Всz информация
                            </h1>
                            <a href='http://127.0.0.1:8000/api/users/' className='btn itd_play text-uppercase'>Перейти</a>
                        </div>

                    </div>

                    <Switch>
                        <Route exact path='/' component={() => <AuthorList users={this.state.users} /> } />

                        <Route exact path='/projects' component={() =>
                            <ProjectsList
                                projects={this.state.projects}
                                findText = {(text) => this.findText(text)}
                                text={this.state.text}
                                deleteProject = {(id)=>this.deleteProject(id)}
                                /> }
                        />

                        <Route exact path='/projects/create' component={() =>
                            <ProjectForm
                                createProject={(project_name, users, link_git, descriptions) =>
                                    this.createProject(project_name, users, link_git, descriptions)}
                                users={this.state.users}
                            /> }
                        />

                        <Route path='/project/:id' component={() =>
                            <ProjectsTodo
                                projects={this.state.projects}
                                todos={this.state.todos}/> }
                        />

                        <Route exact path='/todos' component={() =>
                            <TodosList
                                todos={this.state.todos}
                                deleteToDo = {(id)=>this.deleteToDo(id)}
                            /> }
                        />

                        <Route exact path='/todo/create' component={() =>
                            <ToDoForm
                                createToDo={(description, project, user) => this.createToDo(description, project, user)}
                                users={this.state.users}
                                projects={this.state.projects}
                            />}
                        />

                        <Route exact path='/login' component={() =>
                            <LoginForm
                                get_token={(username, password) => this.get_token(username, password)}
                            />}
                        />

                        <Redirect from='/users' to='/' />
                        <Route component={page_not_found_404} />

                    </Switch>
                </BrowserRouter>

                <Footer/>
			</div>

		)

	}
}


export default App;
