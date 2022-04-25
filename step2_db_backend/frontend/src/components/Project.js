import React from 'react'
import {NavLink} from 'react-router-dom'


const ProjectItem = ({project, deleteProject}) => {

	return (
		<tr>
			<td>
				<NavLink to={`project/${project.id}`}> {project.project_name} </NavLink>
			</td>
			<td>
				{project.users.map((user) => user + ', ')}
			</td>
			<td>
				{project.link_git}
			</td>
			<td>
				{project.descriptions}
			</td>
			<td>
				{project.date_create}
			</td>
			<td>
                <button onClick={() => deleteProject(project.id)}> delete </button>
            </td>
		</tr>
		)
}


const ProjectsList = ({projects, findText, text, deleteProject}) => {

    return(
         <div>

            <form>
                <label>
                        Поиск
                        <input type='text'
                               name="text"
                               value={text}
                               onChange={(event) => findText(event.target.value)}/>
                </label>
            </form>
            <table className='table'>
                <tbody>
                    <tr>
                        <th>
                                название проэкта
                        </th>
                        <th>
                            персонал
                        </th>
                        <th>
                            ссылка в git
                        </th>
                        <th>
                            описание
                        </th>
                        <th>
                            дата создания
                        </th>
                        <th>

                        </th>
                    </tr>

                    {projects.map((project) => <ProjectItem
                                                    key={project.id}
                                                    project={project}
                                                    deleteProject={deleteProject}/>)}
                </tbody>
            </table>
            <NavLink to="projects/create">Создать Project</NavLink>
         </div>
	)
}

export default ProjectsList;