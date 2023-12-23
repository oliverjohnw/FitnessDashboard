console.log('Starting logging')

const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const endBox = document.getElementById('end-box')

const getCookie =(name) =>{
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let visible = 3

const getData = () => {
    $.ajax({
        type: 'GET',
        url: `/data/${visible}`,
        success: function(response){
            console.log('success', response)
            const data = response.workout_data

            setTimeout(() =>{
                spinnerBox.classList.add('not-visible')
                console.log(data)
                data.forEach(el => {
                    let workoutDetails;

                    if (el.exercise === "Weight Lifting") {
                        // Assuming it's a Weight Lifting workout
                        workoutDetails = `
                            <h5 class="card-title">${el.date}: ${el.exercise}</h5>
                            <p class="card-text">${el.time_of_day}</p>
                            <p class="card-text">${el.body_part}</p>
                            <p class="card-text">${el.duration}</p>
                            <p class="card-text">${el.location}</p>
                            <p class="card-text">Mood before: ${el.mood_before}</p>
                            <p class="card-text">Mood after: ${el.mood_after}</p>
                            <p class="card-text">${el.workout_notes}</p>
                        `;
                    }
                    postsBox.innerHTML += `
                        <div class="card mb-2">
                            <div class="card-body">
                                ${workoutDetails}
                            </div>
                            <div class="card-footer">
                                <div class="row">
                                    <div class="col-1">
                                        <a href="#" class="btn btn-primary">Details</a>
                                    </div>
                                    <div class="col-1">
                                        <form class="like-unlike-forms" data-form-id="${el.id}">
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `
                });
            }, 100)
            console.log(response.size)
            if (response.size === 0) {
                endBox.textContent = "No posts added yet..."
            }
            else if (response.size <= visible) {
                loadBtn.classList.add('not-visible')
                endBox.textContent = 'No more posts to load'
            }
        }, 
        error: function(response){
            console.log('error', error)
        }
    })
}

loadBtn.addEventListener('click', ()=>{
    spinnerBox.classList.remove('not-visible')
    visible += 3
    getData()
})

getData()