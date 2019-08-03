import userService from '../../service/UserService';
import userConstants from '../constants/UserConstants';

function getUsers() {
  function success(users) { return { type: userConstants.GET_USERS_SUCCESS, users }; }

  return (dispatch) => {
    userService.getUsers()
      .then((users) => {
        dispatch(success(users.data));
      });
  };
}

export default {
  getUsers
}