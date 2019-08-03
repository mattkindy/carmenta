import userConstants from '../constants/UserConstants';

/* eslint-disable complexity */
function user(state = {}, action) {
  switch (action.type) {
    case userConstants.GET_USERS_SUCCESS:
      return {
        ...state,
        users: action.users,
      };
    default:
      return state;
  }
}

export default user;
