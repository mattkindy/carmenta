import React from 'react';
import { Grid } from '@material-ui/core';
import PropTypes from 'prop-types';
import { bindActionCreators } from 'redux';
// import CandidateItem from './CandidateItem';
import userActions from '../redux/actions/UserActions';
import { connect } from 'react-redux';

class CandidateList extends React.Component {

  componentDidMount() {
    const { actions } = this.props;
    actions.getUsers();
  }

  render() {
    const { userList } = this.props;

    return (
      <Grid>
        {userList.map(user => JSON.stringify(user))}
      </Grid>
    )
  }
}

function mapStateToProps(state) {
  const {
    user: { users = [] },
  } = state;

  return {
    userList: users,
  };
}

function mapDispatchToProps(dispatch) {
  return { actions: bindActionCreators({...userActions}, dispatch) };
}

CandidateList.propTypes = {
  userList: PropTypes.array.isRequired,
}

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(CandidateList);