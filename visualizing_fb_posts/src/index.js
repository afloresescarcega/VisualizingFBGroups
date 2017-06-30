import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class MenuBar extends React.Component {
    render(){
        return (
            <div className="menu-bar">
                <h1>Facebook Group Analyzer</h1>
                <div className="search-icon">
                    <img src="magnifier.png" alt="Search"/>
                </div>
            </div>
        );
    }
}

// export default MenuBar

ReactDOM.render(<MenuBar />, document.getElementById('root'));
