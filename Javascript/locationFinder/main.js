// Listen for submit
document.querySelector('#zipForm').addEventListener('submit', async (event) => {
  event.preventDefault();
  const zip = document.querySelector('#userInput').value

  // Make request to API.
  const res = await fetch(`http://api.zippopotam.us/us/${zip}`);
  if(res.status != 200) {
    document.querySelector('#output').innerHTML =
    `
      <h1 class='center'>Invalid Zipcode, please try again!!</h1>
    `;
    throw Error(res.statusText);
  } else {
    const data = await res.json();
    console.log(data);
    // Show location info.
    let output = ``;
    data.places.forEach(place => {
      output += `
        <article class='center'>
          <ul>
            <li><strong>City: ${place['place name']}</strong></li>
            <li><strong>State: ${place['state']}</strong></li>
            <li><strong>Longitude: ${place['longitude']}</strong></li>
            <li><strong>Latitude: ${place['latitude']}</strong></li>
          </ul>
        </article>
      `
    })
    document.querySelector('#output').innerHTML = output;
  }
})
 
