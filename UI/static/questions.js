function GetMeetupId() {
    var url = window.location.href;
    var meetupid = url.split('=')[1];
    return meetupid;
}

function GetMeetup() {
    let meetup_id = GetMeetupId();
    let url = `https://misocho01-questioner.herokuapp.com/api/v2/meetups/${meetup_id}`;
    fetch(url, {
        methods: GetMeetup,
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then((data) => {
            let meetup = data.data;
            let questions = meetup.questions;
            let meetup_title = meetup.title;
            let image_url = '';
            let date = meetup.happeningon;
            let imageThumbnail = '';
            let splitDate = date.split(' ');
            let month = splitDate[2];
            let questionsHTML = '';
            date = splitDate[1];
            console.log(data);
            if (meetup.images == null) {
                imageThumbnail = `../images/no-image.png`;
            } else {
                url = 'https://i.imgur.com/'
                image_url = meetup.images.replace(url, '');
                file = image_url.split('.');
                fileName = file[0] + 'l';
                fileExtension = file[1];
                imageThumbnail = url + fileName + '.' + fileExtension;

            }
            let image_div = document.getElementById('side-image');
            image_div.style.backgroundImage = `url(${imageThumbnail})`;
            let meetup_details = `<div id="meetup-content">
            <div id="meetup-date">
                <div class="month">${month}</div>
                <div class="date">${date}</div>
            </div>
            <div id="more-meetup-details">
                <div id="meetup-title">
                   ${meetup_title}
                </div>
                <div id="meetup-by">
                    by <span id="host-name">Strathmore GDG</span>
                </div>
            </div>
            <div id="attending">
                <div class="button">
                    <input class="btn" type="button" name="" value="Schedule">
                </div>
            </div>
        </div>`

        for (let i = 0; i < questions.length; i += 1) {
            title = questions[i].question_title;
            votes = questions[i].question_votes;
            body = questions[i].question_body;

            questionsHTML += `<div class="q-list">
            <div class="q-summary">
                <div class="count">
                    <div class="side-count">
                        <div class="total-counts">
                            <span title="votes">${votes}</span>
                        </div>
                        <div>Votes</div>
                    </div>
                </div>
                <div class="summary">
                    <a href="#" class="question">
                        <h3>${title}
                        </h3>
                    </a>
                    <div class="question-description">
                        <span>
                            ${body}
                        <span>
                    </div>
                    <div class="like">
                        <button class="like-btn">
                            <?xml version="1.0" ?>
                            <!DOCTYPE svg
                                PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>
                            <svg enable-background="new 0 0 32 32" height="32px" id="Layer_1"
                                version="1.1" viewBox="0 0 32 32" width="32px" xml:space="preserve"
                                xmlns="http://www.w3.org/2000/svg"
                                xmlns:xlink="http://www.w3.org/1999/xlink">
                                <path
                                    d="M18.221,7.206l9.585,9.585c0.879,0.879,0.879,2.317,0,3.195l-0.8,0.801c-0.877,0.878-2.316,0.878-3.194,0  l-7.315-7.315l-7.315,7.315c-0.878,0.878-2.317,0.878-3.194,0l-0.8-0.801c-0.879-0.878-0.879-2.316,0-3.195l9.587-9.585  c0.471-0.472,1.103-0.682,1.723-0.647C17.115,6.524,17.748,6.734,18.221,7.206z"
                                    fill="" /></svg>
                        </button>
                        <button class="like-btn">
                            <?xml version="1.0" ?>
                            <!DOCTYPE svg
                                PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>
                            <svg enable-background="new 0 0 32 32" height="32px" id="Layer_1"
                                version="1.1" viewBox="0 0 32 32" width="32px" xml:space="preserve"
                                xmlns="http://www.w3.org/2000/svg"
                                xmlns:xlink="http://www.w3.org/1999/xlink">
                                <path
                                    d="M14.77,23.795L5.185,14.21c-0.879-0.879-0.879-2.317,0-3.195l0.8-0.801c0.877-0.878,2.316-0.878,3.194,0  l7.315,7.315l7.316-7.315c0.878-0.878,2.317-0.878,3.194,0l0.8,0.801c0.879,0.878,0.879,2.316,0,3.195l-9.587,9.585  c-0.471,0.472-1.104,0.682-1.723,0.647C15.875,24.477,15.243,24.267,14.77,23.795z"
                                    fill="" /></svg>
                        </button>
                    </div>
                    <div class="comments-box">
                        <button class="comment">comment
                        </button>
                        <a href="#" class="comments">comments<span> 3</span></a>


                        <div class="comment-box">
                            <div class="comment-area">
                                <textarea name="" class="comment-textarea"
                                    placeholder="Comment here"></textarea>

                            </div>
                            <div class="send-icon">
                                <img class="send-img" src="../images/send.svg">
                            </div>
                        </div>
                    </div>
                </div>
            </div>


        </div>`
    }

        document.getElementById('meetup-details').innerHTML = meetup_details;
        document.getElementById('question-list').innerHTML = questionsHTML;
    })
}

window.addEventListener('load', GetMeetup);