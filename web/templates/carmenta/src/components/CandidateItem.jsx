import React from 'react';
import PropTypes from 'prop-types';
import TableCell from '@material-ui/core/TableCell';
import TableRow from '@material-ui/core/TableRow';
import Checkbox from '@material-ui/core/Checkbox';

export default function CandidateItem({ user, isItemSelected, labelId, handleClick }) {
  return (
    <TableRow
      hover
      onClick={event => handleClick(event, user.name)}
      role="checkbox"
      aria-checked={isItemSelected}
      tabIndex={-1}
      key={user.name}
      selected={isItemSelected}
    >
      <TableCell padding="checkbox">
        <Checkbox
          checked={isItemSelected}
          inputProps={{ 'aria-labelledby': labelId }}
        />
      </TableCell>
      <TableCell component="th" id={labelId} scope="row" padding="none">
        {user.name}
      </TableCell>
      <TableCell>{user.title}</TableCell>
      <TableCell>{user.label}</TableCell>
    </TableRow>
  );
}

CandidateItem.propTypes = {
  user: PropTypes.object.isRequired,
  isItemSelected: PropTypes.bool,
  labelId: PropTypes.string.isRequired,
  handleClick: PropTypes.func,
}

CandidateItem.defaultProps = {
  isItemSelected: false,
  handleClick: () => {},
}

