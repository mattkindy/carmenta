import axios from 'axios';

const userApiRoot = '/api/users';

function getUsers() {
  return axios.get(userApiRoot);
}

export default {
  getUsers,
}