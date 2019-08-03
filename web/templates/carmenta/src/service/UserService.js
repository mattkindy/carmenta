import axios from 'axios';

const userApiRoot = '/api/user';

function getUsers() {
  return axios.get(userApiRoot);
}

export default {
  getUsers,
}