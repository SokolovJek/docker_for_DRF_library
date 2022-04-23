import React from 'react'


class ProjectForm extends React.Component {
    constructor(props){
    super(props)
    this.state = {
        project_name: 'add project_name ',
        users: 0,
        link_git: 'https://github.com/',
        descriptions: ''
        };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
    }


    handleChange(event){
        this.setState(
            {[event.target.name]:event.target.value}
        );
    }


    handleSubmit(event){
        event.preventDefault()
        this.props.createProject(
             this.state.project_name,
             this.state.users,
             this.state.link_git,
             this.state.descriptions)
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label htmlFor="project_name">Название проекта</label>
                <br/>
                <input type="text" name="project_name" placeholder="project_name"
                    value={this.state.description} onChange={this.handleChange} />
                <br/>

                <label htmlFor="users">Участник проекта</label>
                <select name="users" className='form-control'
                    onChange={this.handleChange}>
                    {this.props.users.map((item)=>
                        <option  value={item.id} key={item.id}> {item.first_name} </option> ) }
                </select>

                <label htmlFor="link_git">Ссылка на Git </label>
                <br/>
                <input type="text" name="link_git" placeholder="link_git"
                    value={this.state.link_git} onChange={this.handleChange} />
                    <br/>

                <label htmlFor="descriptions">Описание проекта</label>
                <br/>
               <input type="text" name="descriptions" placeholder="descriptions"
                    value={this.state.descriptions} onChange={this.handleChange} />
                    <br/>

               <input type="submit" value="Save" />

            </form>
        );
    }
}

export default ProjectForm