import {dayOfYear, currentDayOfYear} from 'https://deno.land/std@0.63.0/datetime/mod.ts';

console.log(dayOfYear(new Date('2020-08-01')))

console.log(currentDayOfYear())