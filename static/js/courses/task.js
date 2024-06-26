import { renderTaskComments } from './comment.js'
import { createGlobalMessage } from './globalMessage.js'

document.addEventListener('DOMContentLoaded', () => {
      const taskList = document.querySelector('#taskList')
      const TaskContent = document.querySelector('#TaskContent')

      const CourseId = document.querySelector('#CourseId').value
      const TaskId = document.querySelector('#TaskId').value

      const TaskPrevElement = document.querySelector('#TaskPrevElement')
      const TaskNextElement = document.querySelector('#TaskNextElement')
      const TaskContinue = document.querySelector('#TaskContinue')
      const commentList = document.querySelector('#TaskCommentList')
      const taskBookmark = document.querySelector('#taskBookmark')

      const showHideTitleTaskList = document.querySelector('#ShowHideTitleTaskList')
      const TaskPage = document.querySelector('#TaskPage')
      const TaskPageRight = document.querySelector('#TaskPageRight')

      const user__status = document.querySelector('.user__status', 'None')

      const BUTTON_SMILES = {
          Like: '👍',
          Dislike: '👎',
          Heart: '❤️',
          Unicorn: '🦄',
          Clap: '👏',
          Fire: '🔥',
      }

      let current_task = {}
      let all_tasks = []

      const getTaskContent = async () => {
            const getTaskURL = `/api/courses/${CourseId}/tasks/${TaskId}/`
            const response = await fetch(getTaskURL)
            const data = await response.json()

            renderTaskContent(TaskContent, data.data.type, data.data.content)
            renderTaskComments(commentList, data.data.comments, getTaskURL)
            renderTaskBookmark(taskBookmark, data.data.is_bookmarked)
      }

      const renderTaskContent = (place, type, content) => {
            /*
            *     Рендеринг контента задания
            */
            place.innerHTML = ''
            switch (type) {
                  case 'TaskText':
                        renderTextTaskContent(place, content.text)
                        break
                  case 'TaskVideo':
                        renderVideoTaskContent(place, content.video_path)
                        break
                  default:
                        console.log('Type not found!')
            }
      }

      const renderTextTaskContent = (place, text) => {
            /*
            *     Рендеринг текстового задания
            */
            place.innerHTML = text
      }

       const renderVideoTaskContent = (place, video_path) => {
            /*
            *     Рендеринг видео задания
            */
            const video = document.createElement('video')
            video.classList.add('task__page__left__content__video')
            video.src = video_path
            video.controls = true
            place.appendChild(video)
      }

      getTaskContent()

      const getTasks = async () => {
            const response = await fetch(`/api/courses/${CourseId}/titles/`)   
            const data = await response.json()
            renderTitleTasks(data.titles)
      }

      const renderTitleTasks = (titles) => {
            taskList.innerHTML = ''
            titles.forEach(title => {
                  renderTitle(title)
            });

            if (current_task.completed_status !== "Completed" && current_task.type === "TaskText") {
                  complete_task(CourseId, TaskId)
            }

            getPrevNextElements(all_tasks, current_task)
      }

      const renderTitle = (title) => {
            if (title.public) {
                  const div = document.createElement('div')
                  div.classList.add('tasks__title')
                  
                  const div_header = document.createElement('div')
                  div_header.classList.add('tasks__title__header')

                  const div_h3 = document.createElement('h4')
                  div_h3.innerHTML = title.title
                  div.appendChild(div_h3)

                  div_header.appendChild(div_h3)
                  div.appendChild(div_header)

                  title.tasks.forEach((task, index) => {
                        all_tasks.push(task)

                        if (task.id == TaskId) {
                              current_task = task
                        }

                        const div_task = document.createElement('div')
                        div_task.classList.add('task')

                        const div_task__right = document.createElement('div')
                        div_task__right.classList.add('task__left')
                        
                        const div_task_type = document.createElement('span')
                        div_task_type.classList.add('task__done')
                        task.completed_status == 'Completed' ? 
                              div_task_type.style.backgroundColor = '#202020' :
                              div_task_type.style.backgroundColor = 'transparent'
                        div_task__right.appendChild(div_task_type)

                        const div_task_type_a = document.createElement('a')
                        div_task_type_a.innerHTML = task.title
                        div_task_type_a.href=`/courses/${CourseId}/${task.id}/`
                        div_task__right.appendChild(div_task_type_a)

                        if (task.id == TaskId) {
                              div_task_type_a.style.color = '#202020'
                        }

                        const div_task__left = document.createElement('div')
                        div_task__left.classList.add('task__right')
                        div_task__left.innerHTML = `
                              <a href='/courses/${CourseId}/${task.id}/'>
                                    <svg style = "opacity:${task.id == TaskId ? '1': ''} "
                                          width="13.25" 
                                          height="23.75" 
                                          viewBox="0 0 13.25 23.75" fill="none" xmlns="http://www.w3.org/2000/svg">
                                          <path d="M1.26761 1.25L11.8734 11.8558" stroke="#202020" stroke-width="2.8" stroke-linecap="round"/>
                                          <path d="M1.25 22.4146L11.8558 11.8088" stroke="#202020" stroke-width="2.8" stroke-linecap="round"/>
                                    </svg>
                              </a>
                        `

                        div_task.appendChild(div_task__right)
                        div_task.appendChild(div_task__left)
                        
                        div.appendChild(div_task)
                  })

                  taskList.appendChild(div)
            }
      }

      getTasks()

      const complete_task = async (courseId, taskId) => {
            const response = await fetch(`/api/courses/${courseId}/tasks/${taskId}/experiense/`, {
                  method: 'POST',
            })
            const data = await response.json()
      }

      const getPrevNextElements = (all_tasks, current_task) => {
            const index = all_tasks.findIndex(item => item.id === current_task.id);

            if (index === 0) {
                  TaskPrevElement.style.opacity = .5

                  if (all_tasks.length > 1) {
                        let next_page_url = `/courses/${CourseId}/${all_tasks[index + 1].id}/`

                        TaskNextElement.href = next_page_url
                        TaskContinue.href = next_page_url
                  } else {
                        TaskNextElement.style.opacity = .5
                        TaskContinue.style.opacity = .3
                  }
            } else if (index == all_tasks.length - 1) {
                  let prev_page_url = `/courses/${CourseId}/${all_tasks[index-1].id}/`

                  TaskPrevElement.href = prev_page_url
                  TaskNextElement.style.opacity = .5
                  TaskContinue.style.display = 'none'
            } else {
                  let next_page_url = `/courses/${CourseId}/${all_tasks[index+1].id}/`
                  let prev_page_url = `/courses/${CourseId}/${all_tasks[index-1].id}/`

                  TaskPrevElement.href = prev_page_url
                  TaskNextElement.href = next_page_url
                  TaskContinue.href = next_page_url
            }
      }

      const renderTaskBookmark = (button, status) => {
            if (status) {
                button.style.color = '#bba8fd'
            } else {
                button.style.color = '#bcbcbc'
            }
      }

      taskBookmark.addEventListener('click', () => {
            fetch(`/api/courses/${CourseId}/tasks/${TaskId}/bookmarks/`, {
                  method: 'POST'
            })
                .then(response => response.json())
                .then(data => {
                      if (data.message == 'Bookmark added successfully!') {
                            renderTaskBookmark(taskBookmark, true)
                            createGlobalMessage(data.message)
                      } else {
                            renderTaskBookmark(taskBookmark, false)
                            createGlobalMessage(data.message)
                      }
                })
      })

      showHideTitleTaskList.addEventListener('click', () => {
            let menu = TaskPage.querySelector('.task__page__right')

            if (TaskPage.style.gridTemplateColumns === '3fr 1fr'){
                  menu.style.opacity = '0'
                  showHideTitleTaskList.style.rotate = '-90deg'

                  setTimeout(() => {
                        TaskPage.style.gridTemplateColumns = '3fr'
                        menu.style.display = 'none'
                  }, 300)
            } else {
                  TaskPage.style.gridTemplateColumns = '3fr 1fr'
                  menu.style.display = 'flex'

                  setTimeout(() => {
                        menu.style.opacity = '1'
                        showHideTitleTaskList.style.rotate = '0deg'
                  }, 100)
            }
      })

})