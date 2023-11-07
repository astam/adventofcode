module Main exposing (..)

import Array exposing (..)
import Debug exposing (..)
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import List exposing (..)
import Maybe exposing (withDefault)
import Set exposing (..)


type alias Monkey =
    { id : Int
    , items : List Int
    , operation : String
    , test : Int
    , throwToTrue : Int
    , throwToFalse : Int
    }


type alias Monkeys =
    List Monkey


initMonkey : Monkey
initMonkey =
    { id = -1
    , items = []
    , operation = ""
    , test = 10000
    , throwToTrue = -1
    , throwToFalse = -1
    }


addNumber =
    (+) 4


executeOperation : Int -> String -> Int
executeOperation old operation =
    operation
        |> String.split " = "
        |> List.drop 1
        |> List.head
        |> Maybe.withDefault "old * 1"
        |> String.split " "
        |> (\x ->
                case x of
                    [ a, b, c ] ->
                        let
                            defaultValue =
                                if b == "*" then
                                    1

                                else
                                    0

                            arg1 =
                                if a == "old" then
                                    old

                                else
                                    String.toInt a
                                        |> Maybe.withDefault defaultValue

                            arg2 =
                                if c == "old" then
                                    old

                                else
                                    String.toInt c
                                        |> Maybe.withDefault defaultValue
                        in
                        case b of
                            "+" ->
                                arg1 + arg2

                            "*" ->
                                arg1 * arg2

                            _ ->
                                old

                    _ ->
                        old
           )


updateMonkeyItems : Int -> Int -> Monkeys -> Monkeys
updateMonkeyItems id item monkeys =
    case monkeys of
        [] ->
            []

        x :: xs ->
            if x.id == id then
                { x | items = item :: x.items } :: updateMonkeyItems id item xs

            else
                x :: updateMonkeyItems id item xs


decideThrownTo : Int -> Int -> Int -> Int -> Int
decideThrownTo worryLevel divisibleBy ifTrue ifFalse =
    if modBy divisibleBy worryLevel == 0 then
        ifTrue

    else
        ifFalse

inspectItems: Int -> Int -> Int -> Int -> List Int -> List (Int, Int)
inspectItems worryLevel divisibleBy ifTrue ifFalse items =
        case items of
            [] -> []
            x::xs -> 


-- inspectItems: Monkeys -> Monkeys


round monkeys =
    List.range 0 (List.length monkeys)
    |> 



-- case monkeys of
--     [] -> []
--     x::xs ->
-- main : Html msg
-- main =
--     div [ style "font-family" "Courier New, Courier, monospace" ]
--         ([ input
--             |> decodePuzzleInput
--             |> cycleInput
--             |> aggregateInput 0 1
--             |> getEvery40
--             |> getSum
--             |> String.fromInt
--             |> (++) "Score 1: "
--             |> text
--          , br [] []
--          , text "Score 2: "
--          , br [] []
--          ]
--             ++ (input
--                     |> decodePuzzleInput
--                     |> cycleInput
--                     |> aggregateInput 0 1
--                     |> drawPixel
--                     |> drawScreen
--                     |> showDisplay
--                )
--          -- ++ (inputTest2
--          --         |> decodePuzzleInput
--          --         |> cycleInput
--          --         |> aggregateInput 0 1
--          --         |> drawPixel
--          --         |> splitToLines
--          --         |> showDisplay
--          --    )
--         )
-- decodePuzzleInput : String -> List (List String)


decodePuzzleInput puzzleInput =
    puzzleInput
        |> String.split "\n\n"
        |> List.map
            (\x ->
                String.split "\n" x
                    |> List.map String.trim
                    |> List.map (String.split ":")
            )
        |> decodeMonkeyInput


decodeMonkeyInput : List (List (List String)) -> List Monkey
decodeMonkeyInput monkeyInput =
    case monkeyInput of
        [] ->
            []

        x :: xs ->
            decodeMonkeyLine initMonkey x :: decodeMonkeyInput xs


decodeMonkeyLine : Monkey -> List (List String) -> Monkey
decodeMonkeyLine newMonkey monkeyLine =
    case monkeyLine of
        [] ->
            newMonkey

        x :: xs ->
            case x of
                [ y, "" ] ->
                    if String.startsWith "Monkey" y then
                        let
                            monkeyId =
                                String.split " " y
                                    |> List.reverse
                                    |> List.head
                                    |> Maybe.withDefault "-1"
                                    |> String.toInt
                                    |> Maybe.withDefault -1
                        in
                        decodeMonkeyLine { newMonkey | id = monkeyId } xs

                    else
                        decodeMonkeyLine newMonkey xs

                [ "Starting items", y ] ->
                    let
                        monkeyItems =
                            String.split "," y
                                |> List.map String.trim
                                |> List.map
                                    (\z ->
                                        String.toInt z
                                            |> Maybe.withDefault -1
                                    )
                    in
                    decodeMonkeyLine { newMonkey | items = monkeyItems } xs

                [ "Operation", y ] ->
                    decodeMonkeyLine { newMonkey | operation = String.trim y } xs

                [ "Test", y ] ->
                    let
                        test =
                            String.trim y
                                |> String.reverse
                                |> String.words
                                |> List.head
                                |> Maybe.withDefault "0001"
                                |> String.reverse
                                |> String.toInt
                                |> Maybe.withDefault 1000
                    in
                    decodeMonkeyLine { newMonkey | test = test } xs

                [ "If true", y ] ->
                    let
                        throwToTrue =
                            String.trim y
                                |> String.reverse
                                |> String.words
                                |> List.head
                                |> Maybe.withDefault "1-"
                                |> String.reverse
                                |> String.toInt
                                |> Maybe.withDefault newMonkey.id
                    in
                    decodeMonkeyLine { newMonkey | throwToTrue = throwToTrue } xs

                [ "If false", y ] ->
                    let
                        throwToFalse =
                            String.trim y
                                |> String.reverse
                                |> String.words
                                |> List.head
                                |> Maybe.withDefault "1-"
                                |> String.reverse
                                |> String.toInt
                                |> Maybe.withDefault newMonkey.id
                    in
                    decodeMonkeyLine { newMonkey | throwToFalse = throwToFalse } xs

                _ ->
                    decodeMonkeyLine newMonkey xs


inputTest : String
inputTest =
    """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


input : String
input =
    """Monkey 0:
  Starting items: 63, 84, 80, 83, 84, 53, 88, 72
  Operation: new = old * 11
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 1:
  Starting items: 67, 56, 92, 88, 84
  Operation: new = old + 4
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 2:
  Starting items: 52
  Operation: new = old * old
  Test: divisible by 2
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 3:
  Starting items: 59, 53, 60, 92, 69, 72
  Operation: new = old + 2
  Test: divisible by 5
    If true: throw to monkey 5
    If false: throw to monkey 6

Monkey 4:
  Starting items: 61, 52, 55, 61
  Operation: new = old + 3
  Test: divisible by 7
    If true: throw to monkey 7
    If false: throw to monkey 2

Monkey 5:
  Starting items: 79, 53
  Operation: new = old + 1
  Test: divisible by 3
    If true: throw to monkey 0
    If false: throw to monkey 6

Monkey 6:
  Starting items: 59, 86, 67, 95, 92, 77, 91
  Operation: new = old + 5
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 7:
  Starting items: 58, 83, 89
  Operation: new = old * 19
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 1"""
