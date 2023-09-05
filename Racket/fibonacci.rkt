#lang racket

; Computing Fibonacci numbers recursively
; SICP. p. 48 (rus p. 31)

(define (fib-rec n)
    (cond   ((= n 0) 0)
            ((= n 1) 1)
            (else (+    (fib-rec (- n 1))
                        (fib-rec (- n 2))))))


; Computing Fibonacci numbers iteratively
; SICP. p. 50 (rus p. 33)

(define (fib-it n)
    (fib-iter 1 0 n))
(define (fib-iter a b count)
    (if (= count 0)
    b
    (fib-iter (+ a b) a (- count 1))))


(displayln "Fibonacci computing iteratively:")
(displayln (fib-it 45))
(displayln "Fibonacci computing recursively:")
(displayln (fib-rec 45))
