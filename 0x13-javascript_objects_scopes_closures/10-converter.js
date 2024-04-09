#!/usr/bin/node

exports.converter = function (base) {
  function baseConverter (n) {
    return (n.toString(base));
  }

  return baseConverter;
};
