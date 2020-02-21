import ReactDOM from 'react-dom'
import React, { Component } from 'react'


class Test extends React.Component {
  render() {
      return <div><p>hello !!</p></div>;
  }
}

ReactDOM.render(
  <Test/>,
  document.getElementById('react')
);
