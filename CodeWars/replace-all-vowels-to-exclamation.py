<?php

// ! Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

// ! Examples
// * replace("Hi!") === "H!!"
// * replace("!Hi! Hi!") === "!H!! H!!"
// * replace("aeiou") === "!!!!!"
// * replace("ABCDE") === "!BCD!"

function replace(string $s): string {
  // Write your code here
  return preg_replace('/[aeiouAEIOU]/','!',$s);
}
?>