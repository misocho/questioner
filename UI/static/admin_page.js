function PostedMeetups(){
    let url = 'https://misocho01-questioner.herokuapp.com/api/v2/meetups';

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },    
    })
    .then(response => response.json())
    .then((data) => {
        let meetup = data.data;
        let meetupHtml = '';
        for (let i = 0; i < meetup.length; i += 1) {
            let title = meetup[i].title;
            let meetup_id = meetup[i].id;
            let meetup_url = `questions.html?id=${meetup_id}`;

            meetupHtml += ` <div class="meetup-container">
            <li class="list-item"><a href="${meetup_url}">${title}</a>
                <div class="delete-meetup">
                    <div class="delete-icon" onclick=DeleteMeetup(${meetup_id})>
                        <svg id="Layer_1" style="enable-background:new 0 0 64 64;" version="1.1"
                            viewBox="0 0 64 64" xml:space="preserve"
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink">
                            <style type="text/css">
                                .st0 {
                                    fill: #242729;
                                }
                            </style>
                            <g>
                                <g id="Icon-Trash" transform="translate(232.000000, 228.000000)">
                                    <polygon class="st0" id="Fill-6"
                                        points="-207.5,-205.1 -204.5,-205.1 -204.5,-181.1 -207.5,-181.1    " />
                                    <polygon class="st0" id="Fill-7"
                                        points="-201.5,-205.1 -198.5,-205.1 -198.5,-181.1 -201.5,-181.1    " />
                                    <polygon class="st0" id="Fill-8"
                                        points="-195.5,-205.1 -192.5,-205.1 -192.5,-181.1 -195.5,-181.1    " />
                                    <polygon class="st0" id="Fill-9"
                                        points="-219.5,-214.1 -180.5,-214.1 -180.5,-211.1 -219.5,-211.1    " />
                                    <path class="st0"
                                        d="M-192.6-212.6h-2.8v-3c0-0.9-0.7-1.6-1.6-1.6h-6c-0.9,0-1.6,0.7-1.6,1.6v3h-2.8v-3     c0-2.4,2-4.4,4.4-4.4h6c2.4,0,4.4,2,4.4,4.4V-212.6"
                                        id="Fill-10" />
                                    <path class="st0"
                                        d="M-191-172.1h-18c-2.4,0-4.5-2-4.7-4.4l-2.8-36l3-0.2l2.8,36c0.1,0.9,0.9,1.6,1.7,1.6h18     c0.9,0,1.7-0.8,1.7-1.6l2.8-36l3,0.2l-2.8,36C-186.5-174-188.6-172.1-191-172.1"
                                        id="Fill-11" />
                                </g>
                            </g>
                        </svg>
                    </div>
                </div>
            </li>

        </div>`
        }
        document.getElementById('meetups').innerHTML = meetupHtml;
    })
}
window.addEventListener('load', PostedMeetups);