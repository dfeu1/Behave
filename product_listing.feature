Feature: Test product listings at Amazon

Scenario: blenders for sale include Hamilton Beach
    Given that we have gone to wwww.amazon.com
     When we search for "blender"
     Then we find items from "Hamilton Beach"
      And we find items from "Oster"

Scenario: t-shirts for sale include Fruit of the Loom
    Given that we have gone to wwww.amazon.com
     When we search for "t-shirt"
     Then we find items from "Fruit of the Loom"

Scenario Outline: concatenate various things
    Given that we have gone to wwww.amazon.com
     When we search for "<product>"
     Then we find items from "<vendor>"

 Examples: Various products
   | product  | vendor |
   | t-shirts | Hanes  |
   | Apple TV | Apple  | 
   | Echo Dot | Amazon |