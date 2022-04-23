import React from 'react'


class ToDoForm extends React.Component {
    constructor(props){
    super(props)
    this.state = {
        project:  props.projects[0].id,
        user: props.users[0].id,
        todo_description:'dd'
        }
    }

    handleChange(event){
        this.setState(
            {[event.target.name]:event.target.value}
        );
    }

    handleSubmit(event){
        event.preventDefault()
        this.props.createToDo(
             this.state.todo_description,
             this.state.project,
             this.state.user)

    }
    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>

                <label htmlFor="todo_description">Описание ToDo</label>
                <br/>
                <input type="text" name="todo_description" placeholder="todo_description"
                    value={this.state.todo_description} onChange={(event)=>this.handleChange(event)} />
                <br/>

                <label htmlFor="user">Пользователь</label>
                <select name="user" className='form-control'
                    onChange={(event)=>this.handleChange(event)}>
                    {this.props.users.map((item)=> <option
                    value={item.id} key={item.id}> {item.first_name} </option> ) }
                </select>

                <label htmlFor="project">Проект</label>
                <select name="project" className='form-control'
                    onChange={(event)=>this.handleChange(event)}>
                    {this.props.projects.map((item)=> <option
                    value={item.id} key={item.id}> {item.project_name} </option> ) }
                </select>
                <input type="submit" value="Save" />
            </form>
        );
    }
}

export default ToDoForm
