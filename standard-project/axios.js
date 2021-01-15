axios.post('http://127.0.0.1:5000/api/getMovies', {
  movie: 'Father of the Bride Part II'
})
.then((response) => {
  console.log(response);
}, (error) => {
  console.log(error);
});