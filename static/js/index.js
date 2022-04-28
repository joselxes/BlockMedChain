document.addEventListener('DOMContentLoaded', () => {
    var vara=null;
    var today = new Date();
    var user="";

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    // document.querySelector('#yes').disabled = true;
    // document.querySelector('#task').onkeyup = ()=>{
    //
    // }
//
    // When connected, configure buttons
    socket.on('connect', () => {

        // Each button should emit a "submit vote" event
        document.querySelector('#forma').onsubmit = () => {
                // const request = new XMLHttpRequest();
                const contenido = document.querySelector('#mensaje').value;
                const userName = document.querySelector('#yes').dataset.vote;
                user=userName;
                const nombreCanal = document.querySelector('#nombreCanal').innerHTML;
                const time = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate()+" "+today.getHours()+":"+today.getMinutes();
                vara=nombreCanal;
                while ((document.querySelectorAll("li").length)>15) {
                  var elemDel=document.querySelector('li');
                  var ulDel=document.querySelector('ul');
                  ulDel.removeChild(elemDel);
                }

                socket.emit('submit mensaje', {'contenido': contenido,'userName':userName,'nombreCanal':nombreCanal,'time':time});
                return false;

            };

    });

    // When a new vote is announced, add to the unordered list
    socket.on('announce mensaje', data => {
        const li = document.createElement('li');
        const div = document.createElement('div');
        const img = document.createElement('img');
        const p = document.createElement('p');
        const span = document.createElement('span');
        const deslis = document.body.scrollHeight+document.body.offsetHeight;

        const hola=vara==`${data.roomName}`;
        if (hola){

          p.innerHTML = `${data.userName}: ${data.contenido} `;
          if (`${data.userName}`==user) {
            div.className="mensajes";
          }
          else {
            div.className="mensajes darker";
          }


          img.src="/static/imagenes/bandmember.jpg";
          img.alt="Avatar";
          img.style.width='100%';
          span.className="time-right";
          span.innerHTML=`${data.time}`;
          li.appendChild(div);
          div.appendChild(img);
          div.appendChild(p);
          div.appendChild(span);
          document.querySelector('#mens').append(li);
          document.querySelector('#mensaje').value="";
          window.scrollTo(0,deslis);

        }

        else {
          document.querySelector('#mens').append(li);
          document.querySelector('#mensaje').value="";}
          // document.querySelectorAll("li").length //OBTENER NUMERO DE MENSAJES

        }

    );
});
