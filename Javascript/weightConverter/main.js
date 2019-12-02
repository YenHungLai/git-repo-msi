document.querySelector('#output').style.visibility = 'hidden';

document.querySelector('#lbsInput').addEventListener('input', event => {
	document.querySelector('#output').style.visibility = 'visible';
	let lbs = event.target.value;
	document.querySelector('#gramsOutput').innerHTML = lbs / 0.0022046;
	document.querySelector('#kgOutput').innerHTML = lbs / 2.2046;
	document.querySelector('#ozOutput').innerHTML = lbs * 16;
});
