import axios from 'axios';

const userApiRoot = '/api/user';

export function getUsers() {
  return axios.get(userApiRoot);
}