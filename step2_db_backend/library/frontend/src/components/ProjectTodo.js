import React from 'react'
import {useParams} from 'react-router-dom'


const ProjectTodo = ({todo}) => {
	return (
		<tr>
		    <td>
				{todo.id}
			</td>
			<td>
				{todo.project}
			</td>
			<td>
				{todo.users}
			</td>
			<td>
				{todo.todo_descriptions}
			</td>
			<td>
				{todo.date_create}
			</td>
			<td>
				{todo.date_update}
			</td>
			<td>
				{todo.is_active}
			</td>
		</tr>
		)
}


const ProjectsTodo = ({projects, todos}) => {
// функция для вывода всех todo данного проэкта

    let {id} = useParams()         // можно так
//    let my_id = useParams().id    // но так наглядней
    let filter_project = projects.filter((project) => project.id == id)
    let filter_todos = todos.filter((todo) => todo.project == filter_project[0].project_name)
    return(
        <table className='Table'>
            <tbody>
                <tr>
                    <th>
                        id
                    </th>
                    <th>
                        проэкт
                    </th>
                    <th>
                        автор todo
                    </th>
                    <th>
                        описание todo
                    </th>
                    <th>
                        дата создания
                    </th>
                    <th>
                        дата обнавления
                    </th>
                    <th>
                        статус
                    </th>
                </tr>
                {filter_todos.map((todo) => <ProjectTodo todo={todo}/>)}

            </tbody>
        </table>
	)
}

export default ProjectsTodo;
