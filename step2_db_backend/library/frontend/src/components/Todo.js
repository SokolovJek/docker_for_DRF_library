import React from 'react'
import {NavLink} from 'react-router-dom'


const TodoItem = ({todo, deleteToDo}) => {
	return (
            <tr>
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
                    {todo.is_active}
                </td>
                <td>
                    {todo.date_create}
                </td>
                <td>
                    {todo.date_update}
                </td>
                <td>
                    <button onClick={() => deleteToDo(todo.id)}> delete </button>
                </td>
            </tr>
		)
}


const TodosList = ({todos, deleteToDo}) => {
    return(
    <div>
        <table className='table'>
            <tbody>
                <tr>
                    <th>
                          проэкт
                    </th>
                    <th>
                        создатель заметки
                    </th>
                    <th>
                        описание
                    </th>
                    <th>
                        статус
                    </th>
                    <th>
                        дата создания
                    </th>
                    <th>
                        дата обновления
                    </th>
                    <th>

                    </th>
                </tr>
                {todos.map((todo) => <TodoItem key={todo.id} todo={todo} deleteToDo={deleteToDo}/>)}
            </tbody>
        </table>
        <NavLink to="todo/create">Создать ToDo</NavLink>
    </div>
	)
}

export default TodosList;